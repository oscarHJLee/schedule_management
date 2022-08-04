from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Board(TimeStampedModel):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=31)

    class Meta:
        ordering = (
            'created_at',
        )

    def __str__(self):
        return self.title


class Content(TimeStampedModel):
    board = models.ForeignKey('boards.Board', on_delete=models.CASCADE)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = (
            'is_completed',
            'created_at',
        )

    def __str__(self):
        return self.description

    @property
    def comment_list(self):
        return self.comment_set.all()


class Comment(TimeStampedModel):
    content = models.ForeignKey('boards.Content', on_delete=models.CASCADE)
    description = models.TextField()
