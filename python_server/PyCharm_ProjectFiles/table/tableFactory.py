import datetime
htmlTableHeader = '''       <table style="width:100%">
        <tr>
            <th>TrashID</th>
            <th>TrashLevel (cm)</th>
            <th>TrashState</th>
            <th>Last Time Recorded</th>
        </tr>
'''

htmlTableFooter = '''
        </table>'''


class TrashCan:
    def __init__(self, trash_id, trash_level):
        self.trash_id = trash_id
        self.trash_level = trash_level
        self.trash_state = 'Empty'
        self.time = datetime.datetime.now()

    def update_trash_state(self):
        if self.trash_level >= 64:
            self.trash_state = "Empty"
        elif self.trash_level >= 53:
            self.trash_state = "Quarter Full"
        elif self.trash_level >= 42:
            self.trash_state = "Half Full"
        elif self.trash_level >= 31:
            self.trash_state = "Three Quarters Full"
        elif self.trash_level < 31:
            self.trash_state = "Full"


class Table():
    def __init__(self):
        self.numTrashCans = 0
        self.trash_cans = [TrashCan(0, 0)]

    # add trash can to table
    def add_can(self, trash_can):
        self.trash_cans.append(trash_can)
        self.numTrashCans = self.numTrashCans + 1

    # returns html table for trash cans as a string
    def get_table_block(self):
        block = ''
        for can in self.trash_cans:
            block = block + '\n<tr><td>' + str(can.trash_id) + '</td><td>' + str(can.trash_level) + '</td> '
            block = block + '<td>' + can.trash_state + '</td><td>' + str(can.time.strftime("%X")) + '</td></tr>'
        return block
