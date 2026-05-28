import asyncio

import websockets


async def test():

    workflow_id = (
        "220c8ea7-de15-45e5-9d11-8c5ea987ee79"
    )

    uri = (

        f"ws://127.0.0.1:8000/"
        f"ws/workflows/{workflow_id}"
    )

    print(
        f"\nConnecting to:"
    )

    print(uri)

    async with websockets.connect(
        uri
    ) as websocket:

        print(
            "\nConnected!"
        )

        while True:

            message = (
                await websocket.recv()
            )

            print(
                f"\n[EVENT RECEIVED]"
            )

            print(message)


asyncio.run(test())