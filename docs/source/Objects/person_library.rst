

Person
------

.. _Person_Library:

.. _personDescription: 

Description
^^^^^^^^^^^

.. _personLibrary:

Library
^^^^^^^

.. _personMethods:

Methods
^^^^^^^

.. _personConfig:

Configurations
^^^^^^^^^^^^^^

.. _personConnect:

Connection Points
^^^^^^^^^^^^^^^^^

.. _personConstants:

Constants
^^^^^^^^^



.. code-block:: python
    :caption: Spawning a Person 

    QLabsSilhouettePerson().spawn(qlabs, deviceNumber, location, rotation, scale, configuration=0, waitForConfirmation=True)

.. code-block:: python
    :caption: Spawning a Person using Degrees

    QLabsSilhouettePerson().spawn_degrees(qlabs, deviceNumber, location, rotation, scale, configuration=0, waitForConfirmation=True)

.. code-block:: python
    :caption: Making the Person to move to a secondary location

    QLabsSilhouettePerson().move_to(qlabs, deviceNumber, location, speed, waitForConfirmation=True)

