
mkdir ../datasets/
cd ../datasets/
wget https://dds.cr.usgs.gov/download/eyJpZCI6MjkxMzYyNCwiY29udGFjdElkIjoyNDQzNTU1NX0=/
wget https://dds.cr.usgs.gov/download/eyJpZCI6MjkxOTk2OSwiY29udGFjdElkIjoyNDQzNTU1NX0=/
wget https://dds.cr.usgs.gov/download/eyJpZCI6MjkxMzgzNywiY29udGFjdElkIjoyNDQzNTU1NX0=/
tar -zxvf *.gz
rm -rf *.gz
