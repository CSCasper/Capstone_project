
htmlTableHeader = '''       <table style="width:100%">
        <tr>
            <th>TrashID</th>
            <th>TrashLevel</th>
        </tr>
'''

htmlTableFooter = '''
        </table>'''

class TrashCan:
    def __init__(self, trashID, trashLevel):
        self.trashID = trashID
        self.trashLevel = trashLevel


class Table():
    def __init__(self):
        self.numTrashCans = 0
        self.trashCans = [TrashCan(0, 0)]

    def addCan(self, trashCan):
        self.trashCans.append(trashCan)
        self.numTrashCans = self.numTrashCans + 1;

    def getTableBlock(self):
        block = ''
        for can in self.trashCans:
            block = block + '\n<tr><td>'+ str(can.trashID) + '</td>' + '<td>' + str(can.trashLevel) + '</td></tr>'
        return block