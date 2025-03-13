from setuptools import find_packages, setup

package_name = 'int32_topic_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='doraoliver',
    maintainer_email='doracaowei0511@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'int32_publischer = int32_topic_pkg.int32_publischer:main',
            'int32_subscriber = int32_topic_pkg.int32_subscriber:main'
        ],
    },
)
