from orm import create_pool
import asyncio
from models import User
import logging

async def test1(loop):
    await create_pool(loop=loop, host='localhost', port=3306, user='www-data', password='www-data', db='awesome')
    u = User(name='Test19', email='test19@example.com', passwd='123456',
            image='about:blank')
    await u.save()
    print('test ok')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test1(loop))
    loop.close()