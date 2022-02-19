from db_collections.teachers import Teachers


class TeachOperations:

    def teach_main(self):
        """
         Handle's teacher options
        :return:nothing
        """
        option = self.teach_menu()
        while option != 7:
            self.teach_operations(option)
            option = self.teach_menu()
        return

    def teach_menu(self):
        """
        Get's user's option
        :return: user choice
        """
        try:
            user_choice = int(input(f" Press "
                                    "\n 1) Add teacher " +
                                    "\n 2) Add subject to teacher " +
                                    "\n 3) Update teacher " +
                                    "\n 4) Update subject of teacher " +
                                    "\n 5) Delete teacher " +
                                    "\n 6) Print teachers " +
                                    "\n 7) quit " +
                                    "\n"
                                    ))
            return user_choice
        except Exception:
            print("Please select from above")
            return self.teach_menu()

    def teach_operations(self, choice):
        """
        Perform teacher operations based on user selection.
        :param choice: choice of field to edit
        :return: nothing
        """
        teach = Teachers()
        function_dict = {1: teach.add_teacher, 2: teach.add_subject_to_teacher, 3: teach.update_teacher,
                         4: teach.update_subject_of_teacher, 5: teach.delete_teacher, 6: teach.print_teacher}
        function_dict.get(choice)()
