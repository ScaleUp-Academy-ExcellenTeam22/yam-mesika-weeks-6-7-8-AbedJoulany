class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_title: The title of the message.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': message_title,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert (0, message_details)
        else:
            user_box.append (message_details)
        return self.message_id

    def read_inbox(self, username : str, n : int = -1) -> list:
        """
        This function return the N  first messages in the user mail
        :param str username: The message sender's username.
        :param int n: N-th messages to be returned
        :return lst: N-th messages
        :rtype: list

        """
        messages = [msg for msg in self.boxes[username]
        [:n if n != -1 else len(self.boxes[username])] if msg['read'] is False]

        for msg in messages:
            msg['read'] = True

        return messages

    def search_inbox(self, username, string) -> list:
        """
        This function return the user messages that contains the passed string
        :param str username: The message sender's username.
        :param string: string to search within the messages
        :return list: the messages that contains the passed string
        :rtype: list
        """
        return [msg for msg in self.boxes[username] if string.lower() in msg['body'].lower() or
                string.lower() in msg['title'].lower()]


def show_example():
    """Show example of using the PostOffice class."""
    users = ('Newman', 'Mr. Peanutbutter')
    post_office = PostOffice (users)
    message_id = post_office.send_message (
        sender='Mr. Peanutbutter',
        message_title='hi',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    message_id = post_office.send_message (
        sender='Mr. Peanutbutter',
        message_title='hello',
        recipient='Newman',
        message_body='hi, Newman2.',
    )

    print (post_office.read_inbox ('Newman', 1))
    print (post_office.read_inbox ('Newman', 1))
    print (post_office.search_inbox('Newman', 'Hello'))


if __name__ == '__main__':
    show_example ()
