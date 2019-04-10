
htmlTableHeader = '''       <table style="width:100%">
        <tr>
            <th>TrashID</th>
            <th>TrashLevel</th>
        </tr>
'''

htmlTableFooter = '''
        </table>'''


class TrashCan:
    def __init__(self, trash_id, trash_level):
        self.trashID = trash_id
        self.trashLevel = trash_level


class Table():
    def __init__(self):
        self.numTrashCans = 0
        self.trashCans = [TrashCan(0, 0)]

    def add_can(self, trash_can):
        self.trashCans.append(trash_can)
        self.numTrashCans = self.numTrashCans + 1

    def get_table_block(self):
        block = ''
        for can in self.trashCans:
            block = block + '\n<tr><td>'+ str(can.trashID) + '</td>' + '<td>' + str(can.trashLevel) + '</td></tr>'
        return block
