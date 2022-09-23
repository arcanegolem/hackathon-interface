# hackathon-interface

    def show_start_in_status_menu(self, file_name):
        current_time = str(datetime.now().time())
        current_time = current_time[:current_time.find('.')]
        answer = """< body style = " font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;" >
        < p style = " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;" >
        < span style = " color:#ffffff;" >[{}]Детекция медведей в папке - {}...< / span >< / p >< / body >""".format(current_time, file_name)
        self.textBrowser.append(answer)

    def show_data_in_status_menu(self, counter):
        current_time = str(datetime.now().time())
        current_time = current_time[:current_time.find('.')]
        answer = """< body style = " font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;" >
        < p style = " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;" >
        < span style = " color:#ffffff;" >[{}]Найдено: {} < / span >< / p >< / body >""".format(current_time, counter)
        self.textBrowser.append(answer)
