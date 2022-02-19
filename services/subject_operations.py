from db_collections.subjects import Subjects


class SubOperations:

    def sub_main(self):
        """
        Handle's subject options
        :return:nothing
        """
        option = self.sub_menu()
        while option != 6:
            self.sub_operations(option)
            option = self.sub_menu()
        return

    def sub_menu(self):
        """
         Get's user's option
        :return: user choice
        :return:
        """
        try:
            user_choice = int(input(f" Press "
                                    "\n 1) Add subject " +
                                    "\n 2) Update subject " +
                                    "\n 3) Update department of a subject " +
                                    "\n 4) Delete subject " +
                                    "\n 5) Print subjects " +
                                    "\n 6) quit " +
                                    "\n"
                                    ))
            return user_choice
        except Exception:
            print("Please select from above")
            return self.sub_menu()

    def sub_operations(self, choice):
        """
        Perform subject operations based on user selection.
        :param choice: choice of field to edit
        :return: nothing

        """
        sub = Subjects()
        function_dict = {1: sub.add_subject, 2: sub.update_subject, 3: sub.update_department_of_subject,
                         4: sub.delete_subject, 5: sub.print_subject}
        function_dict.get(choice)()
