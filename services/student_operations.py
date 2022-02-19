from db_collections.students import Students


class StudOperations:

    def stud_main(self):
        """
        Handle's Student options
        :return:nothing
        """
        option = self.stud_menu()
        while option != 7:
            self.stud_operations(option)
            option = self.stud_menu()
        return

    def stud_menu(self):
        """
        Get's user's option
        :return: user choice
        """
        try:
            user_choice = int(input(f" Press "
                                    "\n 1) Add student " +
                                    "\n 2) Add teacher to student " +
                                    "\n 3) Update student " +
                                    "\n 4) Update teacher of student " +
                                    "\n 5) Delete student " +
                                    "\n 6) Print student " +
                                    "\n 7) quit " +
                                    "\n"
                                    ))
            return user_choice
        except Exception:
            print("Please select from above")
            return self.stud_menu()

    def stud_operations(self, choice):
        """
        Perform student operations based on user selection.
        :param choice: choice of field to edit
        :return: nothing
        """
        stud = Students()
        function_dict = {1: stud.add_student, 2: stud.add_teacher_to_student, 3: stud.update_student,
                         4: stud.update_teacher_of_student, 5: stud.delete_student, 6: stud.print_student}
        function_dict.get(choice)()
