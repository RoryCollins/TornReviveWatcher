class Member(object):
    def __init__(self, user_id, name, hospitalised, activity_status):
        self.activity_status = activity_status
        self.hospitalised = hospitalised
        self.user_id = user_id
        self.name = name

    def __eq__(self, o: object) -> bool:
        return self.activity_status == o.activity_status and \
            self.hospitalised == o.hospitalised and \
            self.user_id == o.user_id and \
            self.name == o.name
