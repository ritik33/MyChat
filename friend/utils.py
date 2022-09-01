from friend.models import FriendRequest


def get_friend_request_or_false(sender, receiver):
    # check whether friend request exist or not
    try:
        return FriendRequest.objects.get(sender=sender, receiver=receiver, is_active=True)
    except FriendRequest.DoesNotExist:
        return False
