from learning.encapsulation.customer import Customer


class LamtimeFitness(object):
    customers = {}

    def register_customer(self, name, age, gender):
        """
        Register new customers to the system

        :param name: Full Name
        :param age: Age
        :param gender: M = Male, F = Female
        :return: customer_id
        """

        name = name.strip()
        if not (2 < len(name) < 100):
            raise ValueError(
                "Name doesn't match length requirement.  Must be between 2 chars and 100 chars.  Name: {}".format(name))

        if age < 12:
            raise ValueError("Person is too young to register!  Age: ".format(age))

        gender = gender.upper()
        if gender not in ("M", "F"):
            raise TypeError("Incorrect format of gender!  Gender: {}".format(gender))

        customer_id = len(self.customers) + 1
        customer = Customer(customer_id)

        # TODO (2): This is breaking encapsulation.  Let's fix this.
        customer.name = name
        customer.age = age
        customer.gender = gender

        self.customers[customer_id] = customer
        print
        print "customer_id {} registered!".format(customer_id)
        print

        return customer_id

    def display_customer_information(self, customer_id):
        """
        Display customer information

        :param customer_id:
        :return: None
        """

        customer = self.customers[customer_id]

        # TODO (3): This is breaking encapsulation.  Let's fix this.
        print "customer_id: {}".format(customer.customer_id)
        print "name: {}".format(customer.name)
        print "age: {}".format(customer.age)
        print "gender: {}".format(customer.gender)
        print "nickname: {}".format(customer.nickname)
        print "username: {}".format(customer.username)
        print "password: ********"
        print


if __name__ == '__main__':
    system = LamtimeFitness()
    lam_customer_id = system.register_customer("Lam Doan", "24", "M")
    system.customers[lam_customer_id].set_username(lam_customer_id, "lamdoan")
    system.customers[lam_customer_id].set_nickname()
    system.display_customer_information(lam_customer_id)

    dorothy_customer_id = system.register_customer("  Dorothy Young  ", 12, "F")
    system.display_customer_information(dorothy_customer_id)

    john_customer_id = system.register_customer("John Smith", 34, "e")
    system.display_customer_information(john_customer_id)
