from mongodb_object.mongo_object import MongoObject


class Subjects:

    def __init__(self):
        self.mongo_obj = MongoObject()
        self.collection_name = "subjects"

    def add_subject(self):
        """
        Add's subject
        :return: nothing
        """
        try:
            subject_name = input("Please enter subject name to add")
            department_name = input("Please enter subject's department name")
            fetch_query = {"dp_name": department_name}
            dp_id = self.mongo_obj.fetch_value("departments", fetch_query)
            value_to_input = {"sub_name": subject_name, "dp_id": dp_id}
            self.mongo_obj.insert_method(self.collection_name, value_to_input)
        except Exception:
            print("Please enter proper value")

    def update_subject(self):
        """
        update subject
        :return: nothing
        """

        try:
            old_subject_name = input("Please enter old subject name to replace")
            new_subject_name = input("Please enter new subject name")
            where_clause = {"sub_name": old_subject_name}
            value_to_input = {"$set": {"sub_name": new_subject_name}}
            self.mongo_obj.update_method(self.collection_name, where_clause, value_to_input)
        except Exception:
            print("Please enter proper value")

    def update_department_of_subject(self):
        """
        update dp_id
        :return: nothing
        """

        try:
            subject_name = input("Please enter subject name")
            new_department_name = input("Please enter new department name")
            fetch_query = {"dp_name": new_department_name}
            dp_id = self.mongo_obj.fetch_value("departments", fetch_query)
            where = {"sub_name": subject_name}
            value_to_input = {"$set": {"dp_id": dp_id}}
            self.mongo_obj.update_method(self.collection_name, where, value_to_input)
        except Exception:
            print("Please enter proper value")

    def delete_subject(self):
        """
        delete subject
        :return: nothing
        """
        try:
            subject_name = input("Please enter subject name to delete")
            value_to_input = {"sub_name": subject_name}
            self.mongo_obj.delete_method(self.collection_name, value_to_input)
        except Exception:
            print("Please enter proper value")

    def print_subject(self):
        """
        print subject
        :return: nothing
        """
        try:
            for row in self.mongo_obj.print_all(self.collection_name):
                print(row)
        except Exception:
            print("Error at printing subjects")
