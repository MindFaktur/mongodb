from mongodb_object.mongo_object import MongoObject


class Departments:

    def __init__(self):
        self.mongo_obj = MongoObject()
        self.collection_name = "departments"

    def add_department(self):
        """
        Add's department
        :return: nothing
        """
        try:
            department_name = input("Please enter department name to add")
            value_to_input = {"dp_name": department_name}
            self.mongo_obj.insert_method(self.collection_name, value_to_input)
        except Exception:
            print("Please enter proper value")

    def update_department(self):
        """
        update department
        :return: nothing
        """
        try:
            old_department_name = input("Please enter old department name to replace")
            new_department_name = input("Please enter new department name")
            where_clause = {"dp_name": old_department_name}
            action = {"$set": {"dp_name": new_department_name}}

            self.mongo_obj.update_method(self.collection_name, where_clause, action)
        except Exception:
            print("Please enter proper value")

    def delete_department(self):
        """
        delete department
        :return: nothing
        """
        try:
            department_name = input("Please enter department name delete")
            value_to_input = {"dp_name": department_name}
            self.mongo_obj.delete_method(self.collection_name, {value_to_input})
        except Exception:
            print("Please enter proper value")

    def print_department(self):
        """
        print department
        :return: nothing
        """
        try:
            for row in self.mongo_obj.print_all(self.collection_name):
                print(row)
        except Exception:
            print("Error at printing departments")
