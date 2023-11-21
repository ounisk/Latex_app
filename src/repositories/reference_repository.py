#from entities.book import Book
#
class ReferenceRepository:
    def __init__(self):
        self._references = []

    def find_all(self):
        return self._references

    #def find_by_username(self, username):
      #  users = self.find_all()

       # users_with_username = filter(
       #     lambda user: user.username == username,
       #     users
       # )

      #  users_with_username_list = list(users_with_username)

     #   return users_with_username_list[0] if len(users_with_username_list) > 0 else None


    def create(self, book):
        references = self.find_all()

        #existing_user = self.find_by_username(user.username)

        #if existing_user:
         #   raise Exception(
         #       f"User with username {user.username} already exists"
         #   )

        references.append(book)

        self._references = references

        return book
