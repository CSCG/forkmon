from django.db import models

class ForkState(models.Model):
    has_forked = models.BooleanField(default=False)

    def __str__(self):
        return "Has Forked: " + str(self.has_forked)

class Node(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    best_block_hash = models.CharField(max_length=64)
    best_block_height = models.IntegerField()
    prev_block_hash = models.CharField(max_length=64)
    has_reorged = models.BooleanField(default=False)
    is_behind = models.BooleanField(default=False)
    highest_divergence = models.IntegerField(default=0)
    highest_diverged_hash = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return str(self.name)

class Block(models.Model):

    hash = models.CharField(max_length=64)
    height = models.IntegerField()
    prev = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, default=None, blank=True)
    active = models.BooleanField(default=True)
    node = models.ForeignKey(Node)

    def __str__(self):
        return str(self.hash) + " at " + str(self.node)