Architecture
============

The big picture
---------------

  * **FileDecoders**: deal with low level file decoding, dealing with different formats
  * **Notifiers**: deal with notification which can be email, SMS or whatever you implement according to the expected interface

UML diagram
^^^^^^^^^^^

The UML diagram should look like:

::

           ________________                      1:1                           _______________
          |                |------------------------------------------------> | <<interface>> |
          |  FileProcessor |  1:n     _______________                         |  FileDecoder  |
          |________________|-------> | <<interface>> |                        |_______________|
                                     |    notifier   |                            ^ ^ ^
                                     |_______________|                            | | |__________________________
                                         ^  ^  ^                            ______| |_____________               |
                                         |  |  |                      _____|____________    ______|_________     |
                                         |  |  |                     |                  |  |                |
                                         |  |  |_________________    | JSON FileDecoder |  | XML FileDecoder| ...etc
                                 ________|  |________            |   |__________________|  |________________|
                          ______|________     ________|_____     |
                         |               |   |              |
                         | Gmail Notifier|   | SMS Notifier | ...etc
                         |_______________|   |______________|


.. note::

  Note that the relationship between FileProcessor and Notifier is 1:n, which means that a FileProcessor can have several notifiers attached


Interfaces
^^^^^^^^^^

A *FileProcessor* is composed of two objects: a *FileDecoder* and a list of "Notifier*s which are interfaces. Real file decoders and notifiers must implement those interfaces.


Some implementations
--------------------

File decoders
^^^^^^^^^^^^^

.. module :: processfile.decoders.json_decoder
.. autoclass:: JSONFileDecoder

.. module :: processfile.decoders.xml_decoder
.. autoclass:: XMLFileDecoder


Notifiers
^^^^^^^^^

.. module :: processfile.notifiers.gmail_notifier
.. autoclass:: GmailNotifier

.. module :: processfile.notifiers.sms_notifier
.. autoclass:: SMSNotifier
