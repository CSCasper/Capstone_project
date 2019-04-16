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

htmlHistoryHeader = '''       <table style="width:100%">
        <tr>
            <th>Trash Can History</th>
        </tr>
'''

class TrashCan:
    def __init__(self, trash_id, trash_level):
        self.trash_id = trash_id
        self.trash_level = trash_level
        self.trash_state = 'Empty'
        self.time = datetime.datetime.now()

        self.past_states = []

    def update_trash_state(self):
        if self.trash_level >= 64:
            self.trash_state = "Empty"
        elif self.trash_level > 100:
            self.trash_state = "Full"
        elif self.trash_level >= 53:
            self.trash_state = "Quarter Full"
        elif self.trash_level >= 42:
            self.trash_state = "Half Full"
        elif self.trash_level >= 31:
            self.trash_state = "Three Quarters Full"
        elif self.trash_level < 31:
            self.trash_state = "Full"
        else:
            self.trash_state = "Invalid state"

        self.past_states.append(self.generate_log_entry())

    def generate_log_entry(self):
        return str(self.trash_id) + " " + str(self.trash_level) + " " + str(self.time)


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

    def get_history_block_by_id(self, trash_id):
        try:
            block = ""
            for state in self.trash_cans[trash_id].past_states:
                block = block + "\n<tr><td>" + state + "</td></tr>"

            return str(block)
        except:
            print("Error.")
