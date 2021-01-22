#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests.py
========

Created by: hbldh <henrik.blidh@nedomkull.com>
Created on: 2016-02-07, 23:50

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import time

import numpy as np
from scipy.spatial.distance import directed_hausdorff
from math import pi

import pyefd


lbl_1 = 5
img_1 = np.array(
    [
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            191,
            64,
            127,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            0,
            0,
            0,
            127,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            64,
            0,
            0,
            0,
            0,
            64,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            191,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            64,
            127,
            64,
            64,
            0,
            0,
            64,
            191,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            191,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            127,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            64,
            0,
            0,
            127,
            255,
            255,
            191,
            64,
            0,
            0,
            0,
            0,
            0,
            64,
            127,
            127,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            191,
            0,
            0,
            0,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            191,
            0,
            0,
            0,
            64,
            127,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            64,
            0,
            0,
            0,
            0,
            0,
            64,
            191,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            127,
            64,
            0,
            0,
            0,
            0,
            64,
            191,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            191,
            127,
            0,
            0,
            0,
            0,
            127,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            191,
            127,
            0,
            0,
            0,
            64,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            0,
            0,
            0,
            191,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            127,
            0,
            0,
            127,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            127,
            0,
            0,
            127,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            127,
            191,
            255,
            255,
            255,
            255,
            127,
            0,
            0,
            0,
            191,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            127,
            0,
            127,
            255,
            255,
            191,
            64,
            0,
            0,
            0,
            191,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            191,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            127,
            0,
            0,
            0,
            0,
            0,
            0,
            64,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            127,
            0,
            0,
            0,
            64,
            191,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
        [
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
            255,
        ],
    ]
)
contour_1 = np.array(
    [
        [24.0, 13.0125],
        [23.0125, 14.0],
        [23.004188481675392, 15.0],
        [23.0, 15.0125],
        [22.0125, 16.0],
        [22.00313725490196, 17.0],
        [22.0, 17.004188481675392],
        [21.0, 17.004188481675392],
        [20.004188481675392, 18.0],
        [20.0, 18.004188481675392],
        [19.0, 18.006299212598424],
        [18.0, 18.006299212598424],
        [17.0, 18.004188481675392],
        [16.9875, 18.0],
        [16.0, 17.0125],
        [15.993700787401576, 17.0],
        [15.0, 16.006299212598424],
        [14.995811518324608, 16.0],
        [14.9875, 15.0],
        [14.0, 14.0125],
        [13.995811518324608, 14.0],
        [13.9875, 13.0],
        [13.0, 12.0125],
        [12.996862745098039, 12.0],
        [12.993700787401576, 11.0],
        [12.9875, 10.0],
        [12.0, 9.0125],
        [11.0, 9.003137254901961],
        [10.0, 9.006299212598424],
        [9.006299212598424, 10.0],
        [9.003137254901961, 11.0],
        [9.003137254901961, 12.0],
        [9.004188481675392, 13.0],
        [9.0125, 14.0],
        [10.0, 14.9875],
        [10.003137254901961, 15.0],
        [10.003137254901961, 16.0],
        [10.003137254901961, 17.0],
        [10.003137254901961, 18.0],
        [10.003137254901961, 19.0],
        [10.0, 19.0125],
        [9.0125, 20.0],
        [9.006299212598424, 21.0],
        [9.006299212598424, 22.0],
        [9.0, 22.006299212598424],
        [8.9875, 22.0],
        [8.0, 21.0125],
        [7.996862745098039, 21.0],
        [7.996862745098039, 20.0],
        [8.0, 19.9875],
        [8.9875, 19.0],
        [8.9875, 18.0],
        [8.993700787401576, 17.0],
        [8.9875, 16.0],
        [8.0, 15.0125],
        [7.996862745098039, 15.0],
        [7.9875, 14.0],
        [7.0, 13.0125],
        [6.993700787401575, 13.0],
        [6.0, 12.006299212598424],
        [5.993700787401575, 12.0],
        [5.9875, 11.0],
        [5.995811518324607, 10.0],
        [6.0, 9.996862745098039],
        [7.0, 9.9875],
        [7.9875, 9.0],
        [8.0, 8.995811518324608],
        [8.995811518324608, 8.0],
        [9.0, 7.995811518324607],
        [10.0, 7.9875],
        [10.9875, 7.0],
        [11.0, 6.995811518324607],
        [12.0, 6.995811518324607],
        [12.0125, 7.0],
        [13.0, 7.9875],
        [13.003137254901961, 8.0],
        [13.006299212598424, 9.0],
        [13.0125, 10.0],
        [14.0, 10.9875],
        [14.004188481675392, 11.0],
        [14.006299212598424, 12.0],
        [15.0, 12.993700787401576],
        [15.004188481675392, 13.0],
        [15.006299212598424, 14.0],
        [16.0, 14.993700787401576],
        [16.00313725490196, 15.0],
        [17.0, 15.996862745098039],
        [17.006299212598424, 16.0],
        [18.0, 16.993700787401576],
        [19.0, 16.993700787401576],
        [19.993700787401576, 16.0],
        [20.0, 15.993700787401576],
        [20.993700787401576, 15.0],
        [21.0, 14.9875],
        [21.9875, 14.0],
        [21.995811518324608, 13.0],
        [21.99686274509804, 12.0],
        [21.99686274509804, 11.0],
        [21.993700787401576, 10.0],
        [21.0, 9.006299212598424],
        [20.993700787401576, 9.0],
        [21.0, 8.993700787401576],
        [22.0, 8.996862745098039],
        [22.006299212598424, 9.0],
        [23.0, 9.993700787401576],
        [23.006299212598424, 10.0],
        [24.0, 10.993700787401576],
        [24.00313725490196, 11.0],
        [24.00313725490196, 12.0],
        [24.00313725490196, 13.0],
        [24.0, 13.0125],
    ]
)


def test_efd_shape_1():
    coeffs = pyefd.elliptic_fourier_descriptors(contour_1, order=10)
    assert coeffs.shape == (10, 4)


def test_efd_shape_2():
    c = pyefd.elliptic_fourier_descriptors(contour_1, order=40)
    assert c.shape == (40, 4)


def test_normalizing_1():
    c = pyefd.elliptic_fourier_descriptors(contour_1, normalize=False)
    assert np.abs(c[0, 0]) > 0.0
    assert np.abs(c[0, 1]) > 0.0
    assert np.abs(c[0, 2]) > 0.0


def test_normalizing_2():
    c = pyefd.elliptic_fourier_descriptors(contour_1, normalize=True)
    np.testing.assert_almost_equal(c[0, 0], 1.0, decimal=14)
    np.testing.assert_almost_equal(c[0, 1], 0.0, decimal=14)
    np.testing.assert_almost_equal(c[0, 2], 0.0, decimal=14)


def test_normalizing_3():
    # rotate and scale contour_1 by a known amount
    theta = np.radians(30)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c, -s), (s, c))) * 1.5
    contour_2 = np.transpose(np.dot(R, np.transpose(contour_1)))

    c1, t1 = pyefd.elliptic_fourier_descriptors(
        contour_1, normalize=True, return_transformation=True
    )
    c2, t2 = pyefd.elliptic_fourier_descriptors(
        contour_2, normalize=True, return_transformation=True
    )

    # check if coefficients are equal (invariance)
    np.testing.assert_almost_equal(c1, c2, decimal=12)
    # check if normalization parametres match the initial transform
    np.testing.assert_almost_equal(t1[0] * 1.5, t2[0], decimal=12)
    np.testing.assert_almost_equal(
        (t1[1] + np.radians(30)) % (2 * pi), t2[1], decimal=12
    )


def test_locus():
    locus = pyefd.calculate_dc_coefficients(contour_1)
    np.testing.assert_array_almost_equal(locus, np.mean(contour_1, axis=0), decimal=0)


def test_reconstruct_simple_contour():
    simple_polygon = np.array(
        [[1.0, 1.0], [0.0, 1.0], [0.0, 0.0], [1.0, 0.0], [1.0, 1.0]]
    )
    number_of_points = simple_polygon.shape[0]
    locus = pyefd.calculate_dc_coefficients(simple_polygon)
    coeffs = pyefd.elliptic_fourier_descriptors(simple_polygon, order=30)

    reconstruction = pyefd.reconstruct_contour(coeffs, locus, number_of_points)
    # with only 2 decimal accuracy it is a bit of a course test, but it will do
    # directly comparing the two polygons will only work here, because efd coefficients will be cycle-consistent
    np.testing.assert_array_almost_equal(simple_polygon, reconstruction, decimal=2)
    hausdorff_distance, _, _ = directed_hausdorff(reconstruction, simple_polygon)
    assert hausdorff_distance < 0.01


def test_larger_contour():
    locus = pyefd.calculate_dc_coefficients(contour_1)
    coeffs = pyefd.elliptic_fourier_descriptors(contour_1, order=50)
    number_of_points = contour_1.shape[0]

    reconstruction = pyefd.reconstruct_contour(coeffs, locus, number_of_points)
    hausdorff_distance, _, _ = directed_hausdorff(contour_1, reconstruction)
    assert hausdorff_distance < 0.4


def test_performance():
    def for_loop_efd(contour, order=10, normalize=False):
        """Calculate elliptical Fourier descriptors for a contour.
        :param numpy.ndarray contour: A contour array of size ``[M x 2]``.
        :param int order: The order of Fourier coefficients to calculate.
        :param bool normalize: If the coefficients should be normalized;
            see references for details.
        :return: A ``[order x 4]`` array of Fourier coefficients.
        :rtype: :py:class:`numpy.ndarray`
        """
        dxy = np.diff(contour, axis=0)
        dt = np.sqrt((dxy ** 2).sum(axis=1))
        t = np.concatenate([([0.0]), np.cumsum(dt)])
        T = t[-1]

        phi = (2 * np.pi * t) / T

        coeffs = np.zeros((order, 4))
        for n in range(1, order + 1):
            const = T / (2 * n * n * np.pi * np.pi)
            phi_n = phi * n
            d_cos_phi_n = np.cos(phi_n[1:]) - np.cos(phi_n[:-1])
            d_sin_phi_n = np.sin(phi_n[1:]) - np.sin(phi_n[:-1])
            a_n = const * np.sum((dxy[:, 0] / dt) * d_cos_phi_n)
            b_n = const * np.sum((dxy[:, 0] / dt) * d_sin_phi_n)
            c_n = const * np.sum((dxy[:, 1] / dt) * d_cos_phi_n)
            d_n = const * np.sum((dxy[:, 1] / dt) * d_sin_phi_n)
            coeffs[n - 1, :] = a_n, b_n, c_n, d_n

    sample_size = 100

    start = time.time()

    for _ in range(sample_size):
        pyefd.elliptic_fourier_descriptors(contour_1, order=30)

    stop = time.time()
    vectorized_time = stop - start

    print(
        "Time taken to create order 30 efd coefficients for 1000 contours:",
        vectorized_time,
    )

    start = time.time()
    for _ in range(sample_size):
        for_loop_efd(contour_1, order=30)

    stop = time.time()
    for_loop_time = stop - start
    print(
        "Time taken to create order 30 efd coefficients for 100 contours:",
        for_loop_time,
    )
    assert vectorized_time < for_loop_time
