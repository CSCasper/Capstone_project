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


class Table():
    def __init__(self):
        self.numTrashCans = 0
        self.trash_cans = [TrashCan(0, 0)]

    def add_can(self, trash_can):
        self.trash_cans.append(trash_can)
        self.numTrashCans = self.numTrashCans + 1

    def get_table_block(self):
        block = ''
        for can in self.trash_cans:
            block = block + '\n<tr><td>' + str(can.trash_id) + '</td><td>' + str(can.trash_level) + '</td> '
            block = block + '<td>' + can.trash_state + '</td><td>' + str(can.time.strftime("%X")) + '</td></tr>'
        return block
