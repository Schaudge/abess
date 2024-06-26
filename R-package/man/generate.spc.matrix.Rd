% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/generate.spc.matrix.R
\name{generate.spc.matrix}
\alias{generate.spc.matrix}
\title{Generate matrix with sparse principal component}
\usage{
generate.spc.matrix(
  n,
  p,
  support.size = 3,
  snr = 20,
  sigma = NULL,
  sparse.loading = NULL,
  seed = 1
)
}
\arguments{
\item{n}{The number of observations.}

\item{p}{The number of predictors of interest.}

\item{support.size}{A integer specify the number of non-zero entries in the first column of loading matrix.}

\item{snr}{A positive value controlling the signal-to-noise ratio (SNR).
A larger SNR implies the identification of sparse matrix is much easier.
Default \code{snr = Inf} enforces no noise exists.}

\item{sigma}{A numerical vector with length \code{p} specify the standard deviation of each columns.
Default \code{sigma = NULL} implies it is determined by \code{snr}. 
If it is supplied, \code{support.size} would be omit.}

\item{sparse.loading}{A \code{p}-by-\code{p} sparse orthogonal matrix. 
If it is supplied, \code{support.size} would be omit.}

\item{seed}{random seed. Default: \code{seed = 1}.}
}
\value{
A \code{list} object comprising:
\item{x}{An \eqn{n}-by-\eqn{p} matrix.}
\item{coef}{The sparse loading matrix used to generate x.}
\item{support.size}{A vector recording the number of non-zero entries in each .}
}
\description{
Generate simulated matrix that its principal component are
sparse linear combination of its columns.
}
\details{
The methods for generating the matrix is detailedly described in the APPENDIX A: Data generation Section in Schipper et al (2021).
}
\references{
Model selection techniques for sparse weight-based principal component analysis. de Schipper, Niek C and Van Deun, Katrijn. Journal of Chemometrics. 2021. \doi{10.1002/cem.3289}.
}
