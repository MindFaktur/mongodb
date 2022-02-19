from db_collections.departments import Departments


class DpOperations:

    def dp_main(self):
        """
        Handle's Department options
        :return: nothing
        """
        option = self.dp_menu()
        while option != 5:
            self.dp_operations(option)
            option = self.dp_menu()
        return

    def dp_menu(self):
        """
        Get's user's option
        :return: user choice
        """
        try:
            user_choice = int(input(f" Press "
                                    "\n 1) Add Department " +
                                    "\n 2) Update Department " +
                                    "\n 3) Delete Departments " +
                                    "\n 4) Print Departments " +
                                    "\n 5) Quit " +
                                    "\n"
                                    ))
            return user_choice
        except Exception:
            print("Please select from above")
            return self.dp_menu()

    def dp_operations(self, choice):
        """
        Perform department operations based on user selection.
        :param choice: choice of field to edit
        :return: nothing
        """
        dp = Departments()
        function_dict = {1: dp.add_department, 2: dp.update_department,
                         3: dp.delete_department, 4: dp.print_department}
        function_dict.get(choice)()

