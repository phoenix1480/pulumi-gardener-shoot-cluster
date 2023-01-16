from distutils.core import setup
import os.path


PKG = 'gardener-shoot-cluster_provider'


def read_version():
    with open(os.path.join(os.path.dirname(__file__), PKG, 'VERSION')) as version_file:
        version = version_file.read().strip()
    return version


setup(
    name=PKG,
    version=read_version(),
    description='gardener-shoot-cluster Pulumi Provider',
    packages=[PKG],
    package_data={PKG: ['py.typed', 'VERSION', 'schema.json']},
    zip_safe=False,
    install_requires=[
        'pulumi>=3.0.0',
        'pulumi_aws>=5.0.0',
    ],
)
