""" Test SOPT bindings """

def test_sara_wavelets():
    """ Create basis-functions object """
    from nose.tools import assert_equal
    from purify.sopt import BasisFunctions

    shape = 256, 256
    nlevels = 5
    types = ["DB1", "DB2", "DB10", "Dirac"]
    functions = BasisFunctions(shape, nlevels, types)

    assert_equal(len(functions), len(types))
    assert_equal(set([u.name.lower() for u in functions]), set([u.lower() for u in types]))
  
    for wavelet in functions:
        assert_equal(wavelet.nlevels, nlevels)
        assert_equal(wavelet.shape, shape)


def test_sara_analysisop_hardening():
    """ Hardens sopt_sara_analysisop bindings against code changes """
    from numpy import add, exp, arange, mean, max, min
    from numpy.testing import assert_allclose
    from purify.sopt import BasisFunctions

    shape = 256, 256
    nlevels = 4
    types = ["DB1", "DB2", "DB10"]
    functions = BasisFunctions(shape, nlevels, types)

    
    sigma = 10.0, 8.0
    xaxis = (arange(shape[0]) / float(shape[0]) - 0.5) / sigma[0]
    yaxis = (arange(shape[1]) / float(shape[1]) - 0.5) / sigma[1]

    gaussian = exp(-add.outer(xaxis * xaxis, yaxis * yaxis))

    actual = functions.analyze(gaussian)
    
    assert_allclose(
        mean(mean(actual, -1), -1),
        [0.036007226135801075, 0.036007541133741106, 0.03600715848225703] 
    )
    assert_allclose(
        min(min(actual, -1), -1), 
        [-0.00211575115187038, -0.0016413049107621763, -0.000927119110859153]
    )
    assert_allclose(
        max(max(actual, -1), -1), 
        [9.237324386040596, 9.23745215540613, 9.237604022698143]
    )

def test_sara_synthesisop_hardening():
    """ Hardens sopt_sara_synthesisop bindings against code changes """
    from numpy import add, exp, arange, mean, max, min
    from numpy.testing import assert_allclose
    from nose.tools import assert_almost_equal
    from purify.sopt import BasisFunctions

    shape = 256, 256
    nlevels = 4
    types = ["DB1", "DB2", "DB10"]
    functions = BasisFunctions(shape, nlevels, types)

    
    sigma = 10.0, 8.0
    xaxis = (arange(shape[0]) / float(shape[0]) - 0.5) / sigma[0]
    yaxis = (arange(shape[1]) / float(shape[1]) - 0.5) / sigma[1]

    gaussian = exp(-add.outer(xaxis * xaxis, yaxis * yaxis))

    analysis = functions.analyze(gaussian)
    actual = functions.synthesize(analysis)

    assert_allclose(
        mean(mean(analysis, -1), -1),
        [0.5761192143816274, 0.5761192143816207, 0.5761192143816083]
    )
    assert_allclose(
        min(min(analysis, -1), -1), 
        [0.5736634410081112, 0.5736634410081048, 0.5736634410080951] 
    )
    assert_allclose(
        max(max(analysis, -1), -1), 
        [0.5773502691896323, 0.5773502691896251, 0.5773502691896143]
    )

    assert_almost_equal(mean(actual), 0.9978677505256317+0j)
    assert_almost_equal(max(actual), 0.99999999999999689+0j)
    assert_almost_equal(min(actual), 0.99361422627082718+0j)
