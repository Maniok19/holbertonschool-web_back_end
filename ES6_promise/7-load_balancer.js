export default function loadBalancer(chinaDownload, USDownload) {
  const result = Promise.race([chinaDownload, USDownload]);
  return result;
}
