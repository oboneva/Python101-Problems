class ParseData:
    date_delimiter = '==='
    info_delimiter = ','

    def __init__(self, filename):
        self.filename = filename
        self.parsed_data = {}
        self.parse()

    def extract_date(self, string, delimiter):
        return string.split(delimiter)[1].strip()

    def extract_info(self, string, delimiter):
        splited = string.split(delimiter)
        splited = [x.strip()for x in splited]
        return (splited[0], splited[1], splited[2])

    def parse_data_to_dict(self, data):
        lines_data = data.split('\n')
        if len(lines_data) <= 1:
            return

        for line in lines_data:
            if len(line) == 0:
                continue
            elif line.startswith(self.date_delimiter) and line.endswith(self.date_delimiter):

                template_value_for_date_key = [{'income': []}, {'expense': []}]

                current_date = self.extract_date(line, self.date_delimiter)
                self.parsed_data[current_date] = template_value_for_date_key
            else:
                amount, category, category_type = self.extract_info(line, self.info_delimiter)
                amount_category = {'amount': float(amount), 'category': category}
                if category_type == 'New Expense':
                    self.parsed_data[current_date][1]['expense'].append(amount_category)
                elif category_type == 'New Income':
                    self.parsed_data[current_date][0]['income'].append(amount_category)

    def parse(self):
        with open(self.filename, 'a+') as f:
            f.seek(0)
            data = f.read()
            print(data)
        self.parse_data_to_dict(data)

if __name__ == '__main__':
    main()
