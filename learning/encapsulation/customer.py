class Customer(object):
    customer_id = None
    name = None
    age = None
    gender = None
    nickname = None
    username = None
    password = None

    def __init__(self, customer_id):
        self.customer_id = customer_id

    def set_username(self, customer_id, username):
        """
        Update username for customer

        :param customer_id: customer_id
        :param username: desired username
        :return:  None
        """

        self.username = username
        print "Updated customer_id {customer_id}: username = {username}".format(customer_id=customer_id,
                                                                                username=self.username)
        print

    def set_password(self, password):
        """
        Update password for customer

        :param password: desired password
        :return: None
        """

        self.password = password

        print "Updated customer_id {customer_id}: password = ********".format(customer_id=self.customer_id)
        print

    def set_nickname(self):
        """
        Set the nickname as the concatenation of name and age

        :return: None
        """

        # TODO (4): Based on bad coding, this may produce a TypeError.  Implement a logic to handle this exception
        self.nickname = self.name + self.age
        print "Updated customer_id {customer_id}: nickname = {nickname}".format(customer_id=self.customer_id,
                                                                                nickname=self.nickname)
        print

    # TODO (1): Implement getters and setters
