import unittest
from passlib.hash import sha256_crypt
from IRCBoat.Plugins.Auth import User, Auth


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.login = "TEST"
        self.password = "TEST"
        self.level = "0"
        self.nickname = "TEST"
        self.host = "TEST"
        self.user = User.User(
            User.User.separator.join(
                [
                    self.login, User.User.hash_password(self.password),
                    self.level, self.host, self.nickname
                ]))

    def test_create_user(self):
        self.assertEqual(self.login, self.user.login)
        self.assertEqual(self.level, self.user.level)
        self.assertEqual(self.host, self.user.host)
        self.assertEqual(self.nickname, self.user.nickname)

    def test_hash_password(self):
        self.assertTrue(sha256_crypt.verify(self.password, self.user.password))

    def test_check_password(self):
        self.assertTrue(self.user.check_password(self.password))


class UserListTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User.User(User.User.separator.join(
            [
                "TEST", User.User.hash_password("TEST"), "0", "TEST", "TEST"
            ]))
        self.userList = User.UserList('USERS.csv')

    def test_load_user(self):
        f = open('USERS.csv', 'w')
        line = User.User.separator.join([
            "T", User.User.hash_password("T"), "0", "T", "T"
            ])
        f.write(line)
        f.close()
        self.userList = User.UserList('USERS.csv')
        user = self.userList["T"]
        self.assertEqual(user.login, "T")
        self.assertEqual(user.level, "0")
        self.assertEqual(user.host, "T")
        self.assertEqual(user.nickname, "T")

    def test_save_user(self):
        self.userList[self.user.login] = self.user
        self.userList.save()
        f = open('USERS.csv', 'r')
        self.assertEqual(f.readline(), str(self.user))


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.file = "USERS.csv"
        self.auth = Auth.Auth(self.file)
        self.userList = None

    def test_add_user(self):
        self.auth.add_user('T1', 'T1', 1)
        self.assertTrue(self.auth.is_user('T1'))

    def test_delete_user(self):
        self.auth.add_user('T2', 'T2', 1)
        self.auth.delete_user('T2')
        self.assertFalse(self.auth.is_user('T2'))

    def test_update_user(self):
        self.auth.add_user('T3', 'T3', 1)
        self.auth.update_user('T3', level=2)
        self.assertEqual(self.auth.get_user('T3').level)

    def test_is_user(self):
        self.auth.add_user('T4', 'T4', 1)
        self.assertTrue(self.auth.is_user('T4'))

    def test_is_user_connected(self):
        self.auth.add_user('T5', 'T5', 1, 'T5', 'T5')
        self.assertTrue(self.auth.is_user_connected('T5'))

    def test_get_user(self):
        self.atuh.add_user('T6', 'T6', 1, 'T6', 'T6')

if __name__ == '__main__':
    unittest.main()
