from vk_users.vk_users_db import add_users_to_db
from vk_users.requests_to_vk import get_user_info
import time
from vk_users.search_parameters import YEAR_START, YEAR_END


def main():
    print('start collecting')
    count = 0
    returned_quantity = 0
    users_new = []
    sex = [1, 2, 0]
    for s in sex:
        print('in progress...')
        for year in range(YEAR_START, YEAR_END):
            for month in range(1, 13):
                users_new += get_user_info(s, month, year)
                returned_quantity += len(users_new)
                time.sleep(0.34)  # time delay due to api limitations
                count += add_users_to_db(users_new)
                users_new = []

    print(f'{count} new users  are added!\
        (out of {returned_quantity} returned)')
    print('finished')


if __name__ == '__main__':
    main()
