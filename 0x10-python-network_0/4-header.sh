#!/bin/bash
# send GET HTTP request with header variable `X-School-User-Id` of 98
curl -sH 'X-School-User-Id:98' "$1"
