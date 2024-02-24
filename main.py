
import asyncio
import remote_pdb as rpdb
from IPython import embed

async def main():
    rpdb.RemotePdb('127.0.0.1', 8888).set_trace()
    while True:
        print('hello world')
        print("hello again")
        print("goodbye")
    
if __name__ == '__main__':
    # embed()
    asyncio.run(main())
    
# EOF
