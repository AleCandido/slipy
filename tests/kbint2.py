import asyncio
import signal


def close(loop):
    print(f"Finalazing...")
    loop.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, close, loop)
    loop.run_forever()
    loop.close()
    print("Program finished")
