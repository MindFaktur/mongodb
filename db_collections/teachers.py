from mongodb_object.mongo_object import MongoObject


class Teachers:

    def __init__(self):
        self.mongo_obj = MongoObject()
        self.collection_name = "teachers"

    def add_teacher(self):
        """
        Add's teacher
        :return: nothing
        """
        try:
            teacher_name = input("Please enter teacher name to add")
            subject_name = input("Please enter teacher's subject name")
            fetch_query = {"sub_name": subject_name}
            sub_id = self.mongo_obj.fetch_value("subjects", fetch_query)
            value_to_input = {"teacher_name": teacher_name, "sub_id": [sub_id, ]}
            self.mongo_obj.insert_method(self.collection_name, value_to_input)
        except Exception:
            print("Please enter proper value")

    def add_subject_to_teacher(self):
        """
        Add a subject to the subject_id array
        :return: nothing
        """
        try:
            teacher_name = input("Please enter teacher name")
            subject_name = input("Please enter teacher's subject name")
            fetch_query = {"sub_name": subject_name}
            sub_id = self.mongo_obj.fetch_value("subjects", fetch_query)
            where_clause = {"teacher_name": teacher_name}
            add_query = {"$push": {"sub_id": sub_id}}
            self.mongo_obj.update_method(self.collection_name, where_clause, add_query)
        except Exception:
            print("error at adding subject to teacher")

    def update_teacher(self):
        """
        update teacher
        :return: nothing
        """

        try:
            old_teacher_name = input("Please enter old teacher name to replace")
            new_teacher_name = input("Please enter new teacher name")
            where_clause = {"teacher_name": old_teacher_name}
            value_to_input = {"$set": {"teacher_name": new_teacher_name}}
            self.mongo_obj.update_method(self.collection_name, where_clause, value_to_input)
        except Exception:
            print("Please enter proper value")

    def update_subject_of_teacher(self):
        """
        update dp_id
        :return: nothing
        """

        try:
            teacher_name = input("Please enter teacher name")

            old_subject_name = input("Please enter old subject name")
            fetch_query = {"sub_name": old_subject_name}
            old_sub_id = self.mongo_obj.fetch_value("subjects", fetch_query)

            new_subject_name = input("Please enter new subject name")
            fetch_query = {"sub_name": new_subject_name}
            new_sub_id = self.mongo_obj.fetch_value("subjects", fetch_query)

            where_clause = {"teacher_name": teacher_name, "sub_id": old_sub_id}
            value_to_input = {"$set": {"sub_id.$": new_sub_id}}
            self.mongo_obj.update_method(self.collection_name, where_clause, value_to_input)
        except Exception:
            print("Please enter proper value")

    def delete_teacher(self):
        """
        delete teacher
        :return: nothing
        """
        try:
            teacher_name = input("Please enter teacher name to delete")
            value_to_input = {"teacher_name": teacher_name}
            self.mongo_obj.delete_method(self.collection_name, value_to_input)
        except Exception:
            print("Please enter proper value")

    def print_teacher(self):
        """
        print teacher
        :return: nothing
        """
        try:
            for row in self.mongo_obj.print_all(self.collection_name):
                print(f"\n Teacher_name: {row.get('teacher_name')}, teaches: ", end='')
                for i in row.get("sub_id"):
                    fetch_query = {"_id": i}
                    sub_name = self.mongo_obj.fetch_value_by_id("subjects", fetch_query, "sub_name")
                    print(f"{sub_name}, ", end='')

        except Exception:
            print("Error at printing teachers")
