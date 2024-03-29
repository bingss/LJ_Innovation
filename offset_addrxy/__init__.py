# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OffsetAddrXY
                                 A QGIS plugin
 篩選門牌，偏移坐標
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-10-04
        copyright            : (C) 2023 by lin
        email                : lin315307@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load OffsetAddrXY class from file OffsetAddrXY.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .offset_addrXY import OffsetAddrXY
    return OffsetAddrXY(iface)
