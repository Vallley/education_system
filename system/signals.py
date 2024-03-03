from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Product, Users, Groups

@receiver(m2m_changed, sender = Users.product.through)
def new_user_in_product(sender, instance, action, reverse, model, pk_set,  **kwargs):
    if action == 'post_add':
        for p in pk_set:
            m = Product.objects.get(pk=p)
        users_count = Users.objects.filter(product__name = m).count()
        groups = Groups.objects.filter(product__name = m)
        groups_count = groups.count()
        if users_count > 0 and groups_count > 0:
            i = groups[groups_count-1].users.count()
            if i < m.max_group:
                groups[groups_count-1].users.add(instance)
            else:
                new_group = Groups.objects.create(name = m.name + str(groups_count), product = m)
                new_group.users.add(instance)
        else:
            new_group = Groups.objects.create(name = m.name + str(groups_count), product = m)
            new_group.users.add(instance)
                



