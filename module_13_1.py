import asyncio


async def start_strongman(name, power):
    weight_globe = 2
    print(f"Силач {name} начал соревнования.")
    for i in range(5):
        await asyncio.sleep(weight_globe / power)
        print(f'Силач {name} поднял {i+1} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Василий", 3))
    task2 = asyncio.create_task(start_strongman("Иван", 4))
    task3 = asyncio.create_task(start_strongman("Пётр", 5))
    await task1
    await task2
    await task3


if __name__ == '__main__':
    asyncio.run(start_tournament())
