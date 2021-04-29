from setuptools import setup

package_name = 'task2_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aryan',
    maintainer_email='aryangupta973@gmail.com',
    description='Python service client to multiply 2 numbers',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = task2_py.service_member_function:main',
            'client = task2_py.client_member_function:main',
        ],
    },
)
