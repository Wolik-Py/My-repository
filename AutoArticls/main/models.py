from django.db import models

class Article(models.Model):

	article_title = models.CharField( 'Название статьи', max_length = 200)
	article_text = models.TextField('Текст статьи')
	release_date = models.DateField('Дата публикации')

	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = 'Статьи'

class Comment(models.Model):

	Article = models.ForeignKey(Article, on_delete=models.CASCADE)
	name = models.CharField('Авто комментария' , max_length = 50)
	comment_text = models.TextField('Текст комментария')
	release_date_comment = models.DateField('Дата публикации')

	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = 'Комментарии'
