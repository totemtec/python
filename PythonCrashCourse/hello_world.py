unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

def verify_users(unconfirmed_users, confirmed_users):
    while unconfirmed_users:
         current_user = unconfirmed_users.pop()
         print(f"Verifying user: {current_user.title()}")
         confirmed_users.append(current_user)

verify_users(unconfirmed_users[:], confirmed_users)

print(unconfirmed_users)