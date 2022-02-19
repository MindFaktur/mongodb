
from services.department_operations import DpOperations
from services.student_operations import StudOperations
from services.subject_operations import SubOperations
from services.teacher_operations import TeachOperations


class Operations:

    def operation(self):
        """
        Perform operations until the exit value is clicked.
        :return: nothing
        """
        option = self.main_menu()
        exit_at = 5
        while option != exit_at:
            self.menu_operations(option)
            option = self.main_menu()

    def main_menu(self):
        """
                Shows all operations available
                :return: use choice(operation)
                """
        user_choice = int(input(f" Press "
                                "\n 1) Department Operations " +
                                "\n 2) Subject Operations " +
                                "\n 3) Teachers Operations " +
                                "\n 4) Student Operations " +
                                "\n 5) Quit " +
                                "\n "
                                ))

        return user_choice

    def menu_operations(self, choice):
        """
        Directs to sub menu.
        :param choice: Collection to edit
        :return:nothing
        """
        dp = DpOperations()
        sub = SubOperations()
        teach = TeachOperations()
        stud = StudOperations()

        operations_dict = {1: dp.dp_main, 2: sub.sub_main, 3: teach.teach_main, 4: stud.stud_main}
        operations_dict.get(choice)()
