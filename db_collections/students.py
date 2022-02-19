from mongodb_object.mongo_object import MongoObject


class Students:

    def __init__(self):
        self.mongo_obj = MongoObject()
        self.collection_name = "students"

    def add_student(self):
        """
        Add's student
        :return: nothing
        """
        try:
            student_name = input("Please enter student name to add")
            teacher_name = input("Please enter student's teacher name")
            fetch_query = {"teacher_name": teacher_name}
            teacher_id = self.mongo_obj.fetch_value("teachers", fetch_query)
            value_to_input = {"student_name": student_name, "teacher_id": [teacher_id, ]}
            self.mongo_obj.insert_method(self.collection_name, value_to_input)
        except Exception:
            print("Please enter proper value")

    def add_teacher_to_student(self):
        """
        Add a teacher to the teacher_id array
        :return: nothing
        """
        try:
            student_name = input("Please enter student name")
            teacher_name = input("Please enter student's teacher name")
            fetch_query = {"teacher_name": teacher_name}
            teacher_id = self.mongo_obj.fetch_value("teachers", fetch_query)
            where_clause = {"student_name": student_name}
            add_query = {"$push": {"teacher_id": teacher_id}}
            self.mongo_obj.update_method(self.collection_name, where_clause, add_query)
        except Exception:
            print("error at adding teacher to student")

    def update_student(self):
        """
        update student
        :return: nothing
        """

        try:
            old_student_name = input("Please enter old student name to replace")
            new_student_name = input("Please enter new student name")
            where_clause = {"student_name": old_student_name}
            value_to_input = {"$set": {"student_name": new_student_name}}
            self.mongo_obj.update_method(self.collection_name, where_clause, value_to_input)
        except Exception:
            print("Please enter proper value")

    def update_teacher_of_student(self):
        """
        update dp_id
        :return: nothing
        """

        try:
            student_name = input("Please enter student name")

            old_teacher_name = input("Please enter old teacher name")
            fetch_query = {"teacher_name": old_teacher_name}
            old_teacher_id = self.mongo_obj.fetch_value("teachers", fetch_query)

            new_teacher_name = input("Please enter new teacher name")
            fetch_query = {"teacher_name": new_teacher_name}
            new_teacher_id = self.mongo_obj.fetch_value("teachers", fetch_query)

            where_clause = {"student_name": student_name, "teacher_id": old_teacher_id}
            value_to_input = {"$set": {"teacher_id.$": new_teacher_id}}
            self.mongo_obj.update_method(self.collection_name, where_clause, value_to_input)
        except Exception:
            print("Please enter proper value")

    def delete_student(self):
        """
        delete student
        :return: nothing
        """
        try:
            student_name = input("Please enter student name to delete")
            value_to_input = {"student_name": student_name}
            self.mongo_obj.delete_method(self.collection_name, value_to_input)
        except Exception:
            print("Please enter proper value")

    def print_student(self):
        """
        print student
        :return: nothing
        """
        try:
            for row in self.mongo_obj.print_all(self.collection_name):
                print(f"\n Student_name: {row.get('student_name')}, taught by: \n", end='')

                for obj_id in row.get("teacher_id"):
                    fetch_query = {"_id": obj_id}
                    teacher_name = self.mongo_obj.fetch_value_by_id("teachers", fetch_query, "teacher_name")
                    print(f"----- teacher_name: {teacher_name}, teaches subjects: ", end='')
                    subjects = self.mongo_obj.fetch_value_by_id("teachers", fetch_query, "sub_id")

                    for sub_id in subjects:
                        fetch_query = {"_id": sub_id}
                        subject_name = self.mongo_obj.fetch_value_by_id("subjects", fetch_query, "sub_name")
                        print(f"{subject_name}, ", end='')
                    print("-----------")

        except Exception:
            print("Error at printing students")
