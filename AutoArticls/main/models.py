from django.db import models

class Article(models.Model):

	article_title = models.CharField( 'Название статьи', max_length = 200)
	article_text = models.TextField('Текст статьи')
	release_date = models.DateField('Дата публикации')

	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = 'Статьи'

	def __str__(self):
		return self.article_title

class Comment(models.Model):

	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	author_name = models.CharField('Авто комментария' , max_length = 50)
	comment_text = models.TextField('Текст комментария')

	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = 'Комментарии'

	def __str__(self):
		return self.author_name
