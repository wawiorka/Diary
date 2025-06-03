# Digital Diary for Students
## Ученики ведут дневник, прикрепляют задачи, отслеживают цели.
# Темы: 
- [ ] приватность, 
- [ ] CRUD, 
- [ ] напоминания.

https://pypi.org/project/urd/

TypeError: 'class Meta' got invalid attribute(s): index_together


В base/models.py:

строка 148 


class AbstractNotification(models.Model):
строка 236

    class Meta:
        abstract = True
        ordering = ('-timestamp',)
        # speed up notifications count query
        # index_together = ('recipient', 'unread')   # ЗАКОМЕНТИЛА!!! чтобы работали notifications
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')


