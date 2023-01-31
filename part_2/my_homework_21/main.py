from under_main import Store, Shop, Request

store = Store(items={"печенька": 25, "собачка": 25, "елка": 25, "пончик": 3, "зонт": 5, "ноутбук": 1})
shop = Shop(items={"печенька": 2, "собачка": 2, "елка": 2})

# shop = Shop(items={"печенька": 2, "собачка": 2, "елка": 2, "пончик": 2, "зонт": 1, "ноутбук": 1})
storages = {"магазин": shop, "склад": store}


def main():
    print("\nЗдравствуйте!\n")

    while True:
        for storage_name in storages:
            print(f"""Сейчас в  {storage_name}:\n{storages[storage_name].get_items()}""")

        user_input = input("""
        Введите запрос в формате: 'Доставить 2 собачка из склад в магазин'\n
        Введите 'стоп' или 'stop' если хотите закончить: \n
        """)

        if 'stop' in user_input or 'стоп' in user_input:
            break

        try:
            request = Request(request=user_input, storages=storages)

            departure = storages[request.carry_from]
            destination = storages[request.take_to]

            departure.remove(request.product, request.amount)
            destination.add(request.product, request.amount)

        except Exception as e:
            print(e)
            continue

if __name__ == '__main__':
    main()