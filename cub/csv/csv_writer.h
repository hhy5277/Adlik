// Copyright 2019 ZTE corporation. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// The csv format reference https://tools.ietf.org/html/rfc4180

#ifndef CUB_CSV_CSV_WRITER_H
#define CUB_CSV_CSV_WRITER_H

#include <fstream>
#include <string>
#include <vector>

#include "cub/csv/dialect.h"

namespace cub {

struct CSVWriter {
  using Row = std::vector<std::string>;

  CSVWriter(const std::string&);

  Dialect& configureDialect();

  void writeRow(const Row&);

private:
  void writeHeader();
  void writeInternal(const Row&);

  const std::string file_name;
  std::ofstream stream;
  Dialect dialect;
  bool written_header;
};

}  // namespace cub

#endif
