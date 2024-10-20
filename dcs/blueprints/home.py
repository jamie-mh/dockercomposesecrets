from flask import Blueprint, render_template, flash
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms.validators import Length, DataRequired

from dcs import db
from dcs.models.comment import Comment

bp = Blueprint("home", __name__)


class CommentForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(), Length(max=30)])
    content = TextAreaField("content", validators=[DataRequired(), Length(max=200)])
    captcha = RecaptchaField()


@bp.route("/", methods=["GET", "POST"])
def home():
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment()
        comment.name = form.name.data
        comment.content = form.content.data

        db.session.add(comment)
        db.session.commit()

        flash("Thanks for commenting!")
        form = CommentForm(formdata=None)

    comments = db.session.execute(
        db.select(Comment).order_by(db.desc(Comment.created_at))
    ).scalars()

    return render_template("home.jinja", form=form, comments=comments)
