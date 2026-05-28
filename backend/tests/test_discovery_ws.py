import asyncio

import websockets


async def test():

    session_id = (
        "PASTE_SESSION_ID_HERE"
    )

    uri = (

        f"ws://127.0.0.1:8000"
        f"/ws/discovery/{session_id}"
    )

    print(
        f"\nConnecting to:\n{uri}"
    )

    async with websockets.connect(
        uri
    ) as websocket:

        print("\nConnected!")

        while True:

            response = (
                await websocket.recv()
            )

            print(
                f"\nEVENT:\n{response}"
            )


asyncio.run(test())