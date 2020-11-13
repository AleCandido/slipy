# https://stackoverflow.com/a/54528397/8653979

import asyncio


async def main():
    print("Started, press ctrl+C")
    await asyncio.sleep(10)


async def close():
    print("Finalazing...")
    await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        loop.run_until_complete(close())
    finally:
        print("Program finished")
