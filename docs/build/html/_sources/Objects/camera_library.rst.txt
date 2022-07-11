.. _Camera_Library:

Cameras
-------

.. _cameraDescription:

Description
^^^^^^^^^^^

  Cameras work similar to actors on the backend.    


.. _cameraLibrary:

Camera Library
^^^^^^^^^^^^^^

.. autoclass:: library_qlabs_free_camera.QLabsFreeCamera

.. _cameraMethods:

Methods
^^^^^^^

.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.spawn
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.spawn_degrees
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.spawn_and_parent_with_relative_transform
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.spawn_and_parent_with_relative_transform_degrees
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.possess
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.set_camera_properties
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.set_transform

.. _cameraConfigs:

Configurations
^^^^^^^^^^^^^^

There are no configuration options for the camera device.

.. _cameraConnect:

Connection Points
^^^^^^^^^^^^^^^^^

There are no connection points for the free camera device.

.. _cameraConstants:

Constants
^^^^^^^^^

.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.ID_FREE_CAMERA
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_POSSESS
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_POSSESS_ACK
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES_ACK
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_SET_TRANSFORM
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_SET_TRANSFORM_ACK

.. _cameraTutorial:

Camera Tutorial
^^^^^^^^^^^^^^^

:Remarks:



Other Camera Options:

  .. code-block:: python
    :caption: Deleting a Camera
    
      destroy_spawned_actor(classID,deviceNumber)

.. admonition:: Examples

  * **Example 1**
  * **Example 2**
  * **Example 3**

.. dropdown:: Example 1

.. dropdown:: Example 2

.. dropdown:: Example 3


.. tip:: 

  Whatever tips

**See Also:** 

  There is a few steps to initializing a new camera in an environment:

#. Pick a Location for your camera using the :ref:`Coordinate Helper (Determining Locations)` section.
#. Copy the location and rotation desired.
#. Use spawn or spawn_degrees to initialize a new camera. Paste the copied location and rotation into their respective places in the function desired below: